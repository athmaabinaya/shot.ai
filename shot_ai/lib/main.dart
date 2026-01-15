import 'package:flutter/material.dart';
import '../models/digest_items.dart';
import '../services/digest_service.dart';
import '../screens/digest_detail_screen.dart';

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

          return ListView.builder(
            itemCount: items.length,
            itemBuilder: (context, index) {
              final item = items[index];

              return ListTile(
                title: Text(item.title),
                subtitle: Text(
                  'by ${item.author} • ${item.score} points',
                ),
                trailing: const Icon(Icons.arrow_forward_ios, size: 14),
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => DigestDetailScreen(item: item)),
                  );
                },
              );
            },
          );
        },
      ),
    );
  }
}
