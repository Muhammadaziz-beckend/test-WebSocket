const WebSocket = require('ws');

const socket = new WebSocket('ws://localhost:8000/ws/chat/');

// Когда соединение установлено
socket.on('open', function open() {
    console.log("Connection established!");

    // Отправляем сообщение после установки соединения
    socket.send(JSON.stringify({
        'message': 'Hello from WebSocket!'
    }));
});

// Когда приходит сообщение от сервера
socket.on('message', function message(data) {
    const parsedData = JSON.parse(data);
    console.log(parsedData.message); // Выводим полученное сообщение
});

// Обработка ошибок соединения
socket.on('error', function(error) {
    console.log("WebSocket error: " + error.message);
});

// Обработка закрытия соединения
socket.on('close', function(code, reason) {
    console.log(`Connection closed, code=${code}, reason=${reason}`);
});
