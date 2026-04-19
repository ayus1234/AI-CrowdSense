document.addEventListener('DOMContentLoaded', () => {
    // Determine the base URL based on environment. If deployed, it uses empty string (relative paths).
    const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
        ? 'http://127.0.0.1:8080/api' 
        : '/api';

    // 1. Fetch Live Queue Status
    async function fetchQueueStatus() {
        try {
            const res = await fetch(`${API_BASE}/queue-status`);
            const data = await res.json();
            
            const queueContainer = document.getElementById('queue-container');
            queueContainer.innerHTML = ''; // Clear loading
            
            data.forEach(item => {
                let statusClass = 'wait-low';
                if (item.wait > 10 && item.wait <= 15) statusClass = 'wait-medium';
                if (item.wait > 15) statusClass = 'wait-high';
                
                const html = `
                    <div class="queue-item fadeIn">
                        <span class="stall-name">${item.stall}</span>
                        <span class="wait-time ${statusClass}">${item.wait} mins</span>
                    </div>
                `;
                queueContainer.innerHTML += html;
            });
        } catch (error) {
            document.getElementById('queue-container').innerHTML = '<p class="loading" style="color:var(--danger)">Error loading queue data.</p>';
            console.error('Queue Fetch Error:', error);
        }
    }

    // Refresh every 5 seconds
    fetchQueueStatus();
    setInterval(fetchQueueStatus, 5000);

    // 2. Navigation Routing
    const btnRoute = document.getElementById('btn-get-route');
    const selectDest = document.getElementById('destination-select');
    const routeResult = document.getElementById('route-result');

    btnRoute.addEventListener('click', async () => {
        const destination = selectDest.value;
        if (!destination) {
            alert('Please select a destination.');
            return;
        }

        btnRoute.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Loading...';
        btnRoute.disabled = true;

        try {
            const res = await fetch(`${API_BASE}/get-route`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ destination })
            });
            const data = await res.json();
            
            routeResult.innerHTML = `<strong><i class="fa-solid fa-diamond-turn-right"></i> Suggestion:</strong> <br> ${data.suggestion}`;
            routeResult.classList.remove('hidden');
        } catch (error) {
            routeResult.innerHTML = `<span style="color:var(--danger)">Error fetching route.</span>`;
            routeResult.classList.remove('hidden');
        } finally {
            btnRoute.innerHTML = 'Get Route <i class="fa-solid fa-arrow-right"></i>';
            btnRoute.disabled = false;
        }
    });

    // 3. AI Assistant Chat
    const btnAsk = document.getElementById('btn-ask-ai');
    const inputQuestion = document.getElementById('ai-question');
    const chatHistory = document.getElementById('chat-history');

    async function handleAsk() {
        const question = inputQuestion.value.trim();
        if (!question) return;

        // User message
        chatHistory.innerHTML += `<div class="message user-message">${question}</div>`;
        inputQuestion.value = '';
        
        // Typing indicator
        const typingId = 'typing-' + Date.now();
        chatHistory.innerHTML += `<div id="${typingId}" class="message ai-message">Thinking <i class="fa-solid fa-ellipsis fa-fade"></i></div>`;
        chatHistory.scrollTop = chatHistory.scrollHeight;

        try {
            const res = await fetch(`${API_BASE}/ask-ai`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question })
            });
            const data = await res.json();
            
            // Premium delay for "thinking" UX
            await new Promise(resolve => setTimeout(resolve, 1200));
            
            document.getElementById(typingId).remove();
            chatHistory.innerHTML += `<div class="message ai-message">${data.response}</div>`;
        } catch (error) {
            document.getElementById(typingId).remove();
            chatHistory.innerHTML += `<div class="message ai-message" style="color:var(--danger)">Connection error.</div>`;
        }
        
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    btnAsk.addEventListener('click', handleAsk);
    inputQuestion.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleAsk();
    });

    // 4. Welcome Message Typing Effect
    const welcomeMsg = "Hi! I'm your AI event assistant. Need to find the shortest food queue or best exit?";
    const welcomeEl = document.getElementById("welcome-message");
    if (welcomeEl) {
        let textIndex = 0;
        function typeWriter() {
            if (textIndex < welcomeMsg.length) {
                welcomeEl.innerHTML += welcomeMsg.charAt(textIndex);
                textIndex++;
                setTimeout(typeWriter, 40);
            }
        }
        typeWriter();
    }
});
