import 'package:flutter/material.dart';
import '../models/digest_items.dart';
import 'package:url_launcher/url_launcher.dart';

class DigestDetailScreen extends StatelessWidget {
  final DigestItem item;

  const DigestDetailScreen({super.key, required this.item});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('shot.ai')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: ListView(
          children: [
            Text(item.title,
                style: Theme.of(context).textTheme.headlineSmall),
            const SizedBox(height: 12),
            Text(item.summary),
            const SizedBox(height: 20),
            if (item.url != null)
              TextButton(
                onPressed: () => launchUrl(Uri.parse(item.url!)),
                child: const Text('Read original'),
              )
          ],
        ),
      ),
    );
  }
}
