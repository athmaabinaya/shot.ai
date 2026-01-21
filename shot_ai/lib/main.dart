import 'package:flutter/material.dart';
import '../models/digest_items.dart';
import '../services/digest_service.dart';
import 'package:url_launcher/url_launcher.dart';

void main() {
  runApp(const ShotAIApp());
}

class ShotAIApp extends StatelessWidget {
  const ShotAIApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'shot.ai',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: Colors.deepPurple,
        scaffoldBackgroundColor: const Color(0xFFF6F7FB),
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
        title: const Text(
          'shot.ai',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        backgroundColor: Colors.indigo[200],
        elevation: 1,
      ),
      body: FutureBuilder<List<DigestItem>>(
        future: digestFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }

          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }

          final items = snapshot.data!;

          return ListView.separated(
            padding: const EdgeInsets.all(12),
            itemCount: items.length,
            separatorBuilder: (_, __) => const SizedBox(height: 20),
            itemBuilder: (context, index) {
              final item = items[index];

              return _DigestCard(item: item);
            },
          );
        },
      ),
    );
  }
}

class _DigestCard extends StatelessWidget {
  final DigestItem item;

  const _DigestCard({required this.item});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
      elevation : 2,
      child: Theme(
        data: Theme.of(context).copyWith(
          dividerColor: Colors.transparent, // remove default divider
        ),
        child: ExpansionTile(
          maintainState: true,
          tilePadding:
          const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          childrenPadding:
          const EdgeInsets.fromLTRB(16, 0, 16, 16),

          title: Text(
            item.title ?? "Untitled",
            style: const TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),

          subtitle: Text(
            item.source == "GitHub Trending"
                ? "${item.source ?? "Untitled"} • ⭐ ${item.stars ?? 0} stars"
                : "${item.source ?? "UNKNOWN"} • Score: ${item.score ?? 0}",
            style: const TextStyle(
              fontSize: 12,
              color: Colors.grey,
            ),
          ),

          children: [
            Text(
              item.summary ?? "No summary available",
              textAlign: TextAlign.left,
              style: const TextStyle(
                fontSize: 14,
                height: 1.45,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
