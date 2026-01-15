class DigestItem {
  final int id;
  final String title;
  final String? url;
  final String author;
  final int score;
  final String summary;


  DigestItem({
    required this.id,
    required this.title,
    required this.url,
    required this.author,
    required this.score,
    required this.summary,
  });

 factory DigestItem.fromJson(Map<String, dynamic> json) {
  return DigestItem(
    id: json['id'],
    title: json['title'] ?? 'Untitled',
    url: json['url'],
    author: json['by'] ?? 'unknown',  
    score: json['score'] ?? 0,
    summary: json['summary'] ?? 'No summary available.',
  );
}
}
