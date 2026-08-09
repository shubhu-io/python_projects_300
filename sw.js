const inputResolvers = new Map();

self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);
    if (url.pathname === '/_python_input') {
        const id = url.searchParams.get('id');
        
        event.respondWith(new Promise((resolve) => {
            // Store the resolver function to respond when input is provided
            inputResolvers.set(id, (text) => {
                resolve(new Response(text, {
                    status: 200,
                    headers: { 
                        'Content-Type': 'text/plain',
                        'Cache-Control': 'no-store'
                    }
                }));
            });
            
            // Notify clients (main thread) that input is requested
            self.clients.matchAll().then(clients => {
                clients.forEach(client => {
                    client.postMessage({ type: 'INPUT_REQUESTED', id: id });
                });
            });
        }));
    }
});

self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'INPUT_PROVIDED') {
        const resolver = inputResolvers.get(event.data.id);
        if (resolver) {
            resolver(event.data.text);
            inputResolvers.delete(event.data.id);
        }
    }
});
