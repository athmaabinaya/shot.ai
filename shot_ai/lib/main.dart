import 'package:flutter/material.dart';

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

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('shot.ai'),
      ),
      body: const Center(
        child: Text(
          'Your daily shot of tech.\nComing soon.',
          textAlign: TextAlign.center,
        ),
      ),
    );
  }
}
