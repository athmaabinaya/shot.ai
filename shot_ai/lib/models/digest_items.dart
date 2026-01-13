class DigestItem {
  final int id;
  final String title;
  final String? url;
  final String author;
  final int score;

  DigestItem({
    required this.id,
    required this.title,
    required this.url,
    required this.author,
    required this.score,
  });

  factory DigestItem.fromJson(Map<String, dynamic> json) {
    return DigestItem(
      id: json['id'],
      title: json['title'],
      url: json['url'],
      author: json['by'],
      score: json['score'],
    );
  }
}
