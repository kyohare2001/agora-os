'use client';

import { useState } from 'react';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  const [thought, setThought] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Implement thought submission
    console.log('Submitting thought:', thought);
  };

  return (
    <main className={`min-h-screen p-8 ${inter.className}`}>
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center">
          Agora AI
        </h1>
        <p className="text-xl text-gray-600 mb-8 text-center">
          思想と思想が交差し、深まり合う"対話空間"
        </p>

        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <form onSubmit={handleSubmit} className="space-y-4">
            <textarea
              className="w-full h-32 p-4 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="あなたの思考や問いを共有してください..."
              value={thought}
              onChange={(e) => setThought(e.target.value)}
            />
            <button
              type="submit"
              className="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors"
            >
              思考を共有する
            </button>
          </form>
        </div>

        <div className="space-y-4">
          {/* Sample thoughts - will be replaced with real data */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <p className="text-gray-800">
              「テクノロジーと人間性の関係について、どのように考えればよいのだろうか？」
            </p>
            <div className="mt-4 flex items-center text-sm text-gray-500">
              <span>user1</span>
              <span className="mx-2">•</span>
              <span>2024-04-01</span>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
