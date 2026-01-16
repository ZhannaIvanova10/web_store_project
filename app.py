"""
Простое веб-приложение для домашнего задания.
На любой GET-запрос возвращает страницу 'Контакты'.
"""
import http.server
import socketserver
import json
from urllib.parse import parse_qs

PORT = 8000

class WebStoreHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Обработка GET-запросов"""
        print(f"📨 GET запрос: {self.path}")
        
        # Всегда возвращаем страницу контактов
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        try:
            with open('pages/contacts.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            self.wfile.write(html_content.encode('utf-8'))
            print("✅ Страница 'Контакты' отправлена")
        except FileNotFoundError:
            self.wfile.write(b'<h1>Ошибка: файл не найден</h1>')
    
    def do_POST(self):
        """Обработка POST-запросов (доп. задание)"""
        print(f"📨 POST запрос: {self.path}")
        
        # Получаем данные
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Выводим в консоль
        print("📝 Полученные данные:")
        print(post_data.decode('utf-8'))
        print("─" * 40)
        # Отправляем ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')

def main():
    """Запуск сервера"""
    with socketserver.TCPServer(("", PORT), WebStoreHandler) as httpd:
        print(f"🚀 Сервер запущен: http://localhost:{PORT}")
        print("🛑 Ctrl+C для остановки")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
