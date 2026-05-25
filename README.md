# Отчет: Реализация Service (Client + Server)

**Описание**
Был реализован простой клиент-серверный сервис с использованием Node.js. Сервер поднимается на порту 3000 и обрабатывает GET-запросы, возвращая JSON-ответ. Клиент использует встроенный метод fetch для отправки запроса и выводит полученный ответ в консоль.

## Демонстрация работы
Ниже представлен скриншот терминалов: снизу запущен сервер, ожидающий подключений, сверху — выполнение скрипта клиента и получение ответа.
###[screenshot.jpg]

## Исходный код

### server.js
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    if (req.method === 'GET' && req.url === '/api/ping') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Hello from Server!', status: 'Success' }));
    } else {
        res.writeHead(404);
        res.end();
    }
});

server.listen(3000, () => {
    console.log('[Server] Listening on port 3000...');
});
