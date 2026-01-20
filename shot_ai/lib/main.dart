import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import '../models/digest_items.dart';
import '../services/digest_service.dart';

void main() {
  runApp(const ShotAIApp());
}

class ShotAIApp extends StatelessWidget {
  const ShotAIApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'shot.ai',
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: Colors.deepPurple,
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late Future<List<DigestItem>> digestFuture;

  @override
  void initState() {
    super.initState();
    digestFuture = DigestService.fetchDigest();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('shot.ai — Daily Shot'),
      ),
      body: FutureBuilder<List<DigestItem>>(
        future: digestFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }

          final items = snapshot.data!;
          if (items.isEmpty) {
            return const Center(child: Text('No items available.'));
          }

          return ListView.builder(
            itemCount: items.length,
            itemBuilder: (context, index) {
              final item = items[index];

              return Card(
                margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
                child: Padding(
                  padding: const EdgeInsets.all(12.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Title clickable link
                      GestureDetector(
                        onTap: () async {
                          if (item.url != null &&
                              await canLaunchUrl(Uri.parse(item.url!))) {
                            await launchUrl(Uri.parse(item.url!));
                          }
                        },
                        child: Text(
                          item.title ?? "Untitled",
                          style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: Colors.blueAccent,
                            decoration: TextDecoration.underline,
                          ),
                        ),
                      ),
                      const SizedBox(height: 4),

                      // Source + Score
                      Text(
                        item.source == "GitHub Trending"
                          ? '${item.source ?? "Untitled"} • ⭐ ${item.stars ?? 0} stars'
                          :'${item.source ?? "UNKNOWN"} • Score: ${item.score ?? 0}',
                        style:
                            const TextStyle(fontSize: 12, color: Colors.grey),
                      ),
                      const SizedBox(height: 8),

                      // Summary
                      Text(
                        item.summary ?? 'Summary temporarily unavailable',
                        style: const TextStyle(fontSize: 14),
                      ),
                    ],
                  ),
                ),
              );
            },
          );
        },
      ),
    );
  }
}
