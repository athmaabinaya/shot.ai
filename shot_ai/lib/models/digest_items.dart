class DigestItem {
  final String? title;
  final String? url;
  final String? source;
  final String? category;
  final String? summary;
  final int? stars;
  final int? score;

  DigestItem({
    this.title,
    this.url,
    this.source,
    this.category,
    this.summary,
    this.stars,
    this.score,
  });

  factory DigestItem.fromJson(Map<String, dynamic> json) {
    try {
      print("Parsing JSON: $json"); // DEBUG: prints every item
      return DigestItem(
        title: json['title'] as String?,
        url: json['url'] as String?,
        source: json['source'] as String?,
        category: json['category'] as String?,
        summary: json['summary'] as String?,
        stars: json['stars'],
        score: json['score'] as int?,
      );
    } catch (e, stack) {
      print("Error parsing DigestItem: $e");
      print(stack); // full trace
      rethrow;       // optional: stops execution so you can see which line
    }
  }
}
