
# sakuracloud-maintenance-checker
さくらクラウドのメンテナンス情報の有無をチェックする。  

## 機能

 * 引数にIPを利用する。
 * さくらのクラウドのAPIを利用して、インスタンスのメンテナンス情報を参照する。

## 動作用件

 * Python3
 * Ubuntu20.04
### 注意事項
- 検索するIPアドレスはさくらのクラウドのコンパネに登録されている必要があります。
  サーバー内部で独自に設定されたVPNやローカルIPは検索できません。
- ローカルIPの検索にも対応していますが、複数のサーバーでヒットした場合にはエラーが返ります。

## 設定

 スクリプト内のapi情報を書き換える。  
 APIキーのアクセスレベルはリソース閲覧以上が必要。

  |変数|設定値|
  |---|---|
  |apikey|さくらのクラウドのアクセストークン|
  |apisecret|さくらのクラウドのアクセストークンシークレット|
  |url|さくらのクラウドのAPI URL|


## CLI

 ```
 ./check.py InstanceIP
 ```
 * メンテナンス情報がある場合は対象URLが出る。
 * メンテナンス情報がない場合は"Nothing information!"を返す。
 * エラーの場合は内容に応じたメッセージが出る。
    * "API key not exist." API情報が空のときに表示される。
    * "Http request error." サーバーと接続できなかったときなどに表示される。
    * "API server error Code" APIserverから200以外のステータスが返ったときに表示される。
    * "Json format error." サーバーから取得したデータがJSONとして認識できないときに表示される。
    * "Not enough arguments." 引数をつけずに実行したときに表示される。
    * "IP address not found." 指定したIPアドレスのサーバが存在しないときに表示される。
    * "Found multiple servers." 複数のサーバーが見つかったときに表示される。
    * "Host server error. (server may be powered off)" ホストサーバーの情報を取得できなかったときに表示される。


## 参考
https://developer.sakura.ad.jp/cloud/api/1.1/