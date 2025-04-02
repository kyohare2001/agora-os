# Agora AI

思想と思想が交差し、深まり合う"対話空間"をAIと共に創るプラットフォーム。

## ✨ コンセプト

現代のSNSが"意見のぶつけ合い"や"承認欲求の応酬"に陥りがちな中で、個人の思想や問いがじっくり熟成され、他者と交差する場としての「現代のアゴラ（広場）」を、AIの力を使って再定義します。

## 🚀 主な機能

1. 思考スレッド投稿（Thread of Thought）
   - 完成された意見ではなく「問い」「違和感」「思考のメモ」をポスト
   - 思考の過程を重視した投稿形式

2. AIによる問いの深化・整理
   - 投稿された問いや思考に対し、AIが関連文献・概念・反論視点などを提案
   - 思考を深めるためのサポート

3. 共鳴と対話（Resonance + Reflect）
   - "いいね"ではなく、共鳴・問い返し・内省の共有といった"対話ベースの反応"
   - 深い対話を促進する仕組み

4. 思想プロフィール
   - ユーザーの思考ログが蓄積され、自分の思想の変遷を時系列で確認可能
   - 思考の成長を可視化

## 🛠️ 技術スタック

### フロントエンド
- Next.js 14
- TypeScript
- Tailwind CSS
- React Query

### バックエンド
- FastAPI
- Python 3.10+
- Supabase
- OpenAI API
- LangChain

## 🚀 開発環境のセットアップ

### 必要条件
- Node.js 18+
- Python 3.10+
- npm or yarn
- Supabase アカウント
- OpenAI API キー

### フロントエンドのセットアップ

```bash
cd frontend
npm install
npm run dev
```

### バックエンドのセットアップ

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 環境変数の設定

1. バックエンドの `.env` ファイルを設定
2. フロントエンドの環境変数を設定

## 📝 開発ガイドライン

- コミットメッセージは日本語で記述
- プルリクエストは日本語で説明
- コードコメントは日本語で記述
- 変数名・関数名は英語で記述

## 🤝 コントリビューション

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m '素晴らしい機能を追加'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

