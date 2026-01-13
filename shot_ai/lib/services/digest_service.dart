import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/digest_items.dart';

class DigestService {
  static const String baseUrl = 'http://localhost:8000';// Android emulator

  static Future<List<DigestItem>> fetchDigest() async {
    final response = await http.get(Uri.parse('$baseUrl/digest'));

    if (response.statusCode != 200) {
      throw Exception('Failed to load digest');
    }

    final data = json.decode(response.body);
    final List items = data['items'];

    return items.map((e) => DigestItem.fromJson(e)).toList();
  }
}
