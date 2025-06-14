# MCP × FizzBuzz PoC

## 🎯 目的
LLM（ローカル推論）＋MCP的実行環境を使って、自然言語からFizzBuzzのコードを自動生成・実行するPoCを構築する。

## 🧪 想定構成
- LLM: Ollama + LLama3 または Mistral
- LangChain: プロンプトテンプレート生成用
- 実行環境: Python exec()（制限付き）
- UI: Streamlitまたは簡易CLI
- セキュリティ: 実行コードをログに記録、内容チェックあり

## 🔄 フロー（予定）
1. 「FizzBuzzを出力して」と自然言語で入力
2. LLMがPythonコードを生成
3. 生成コードを実行
4. 結果を画面に出力（＋ログ保存）

## ✅ TODO（初期）
- [ ] README に構成と目的を書く（済）
- [ ] LangChain + LLM の簡易実行環境準備
- [ ] exec()用の安全なスクリプト実行制御
- [ ] プロンプトテンプレート作成
- [ ] UIのプロトタイプ（Streamlit or CLI）

## 📁 今後の構成（予定）
- `main.py`：実行用スクリプト
- `prompt_template.txt`：LLMへの入力テンプレート
- `exec_sandbox.py`：安全なコード実行ラッパー
- `result_log.txt`：実行結果ログ

