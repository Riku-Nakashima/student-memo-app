\## 生徒メモ管理アプリ
# 主な機能
- 生徒の登録・一覧表示・削除
- 生徒名による検索機能
- 生徒ごとの指導メモ（教科・日付・内容）の追加
- 指導メモの一覧表示・削除
   
# 使用技術
- Python 3
- Flask
- SQLite3
- HTML / CSS
  
# データベース設計
- students テーブル
  - id (PK)
  - name
  - grade

- notes テーブル
  - id (PK)
  - student_id (FK)
  - date
  - subject
  - content

students と notes は 1 対 多 の関係になっています。

# 起動方法
1. リポジトリをクローンする
- git clone https://github.com/Riku-Nakashima/student-memo-app.git
- cd student-memo-app
2. 必要なライブラリをインストール
- pip install flask
3. データベースを初期化
- python init_db.py
4. アプリを起動
- python app.py
5. ブラウザで以下にアクセス  
- http://localhost:5000

## 今後の改善点
- ログイン機能の追加
- 教科の追加・編集機能
- PostgreSQLへの移行



