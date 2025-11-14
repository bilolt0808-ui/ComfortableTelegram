// Отправка сообщения через ваш сервер
void sendMessage(String text, String chatId) async {
  await http.post(
    Uri.parse('https://your-server.com/send_message'),
    body: jsonEncode({'chat_id': chatId, 'text': text}),
  );
}