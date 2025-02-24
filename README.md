![badge](https://img.shields.io/badge/Python-white?logo=python) 
![badge](https://img.shields.io/badge/preset-red) 
[![badge](https://img.shields.io/badge/Package_manager-uv-8A2BE2)](https://docs.astral.sh/uv/) ![badge](https://img.shields.io/badge/Linter-Ruff-yellow)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Yoshida24/preset-python-uv)

# duckdb-minio

DuckDB + MinIO の組み合わせを試すためのリポジトリ

## duckdb をローカルにインストールしてMinIO経由で使ってみる
S3互換APIでParquetのデータを読めることを確認する。
ローカルにDuckDBをインストールする

```bash
brew install duckdb
# duckdb --version   
# v1.2.0 5f5512b827
```

MinIOをdocker composeで立ち上げる。

```bash
docker compose up
```

データをDuckDBに入れる:

```
$ duckdb
v1.2.0 5f5512b827
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D CREATE SECRET minio (
    TYPE S3,
    KEY_ID 'duckdb-local',
    SECRET 'duckdb-local',
    ENDPOINT '127.0.0.1:9000',
    USE_SSL false,
    URL_STYLE 'path'
  );
D COPY (SELECT * FROM parquet_scan('https://duckdb-wasm.shiguredo.jp/P78BHZM3MD3MV47JDZG47PB8PW.parquet')) TO "s3://duckdb-local/spam.parquet" (FORMAT parquet, COMPRESSION zstd);
```

Parquetのデータをクエリできるか確認する:

```bash
$ duckdb
v1.2.0 5f5512b827
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D SELECT * FROM parquet_scan("s3://duckdb-local/spam.parquet");

┌──────────────────────┬──────────────────────┬─────────────────┬───┬──────────────────────┬───────────────────┬─────────────────────┐
│    connection_id     │          id          │      label      │ … │        rtc_id        │   rtc_timestamp   │      rtc_type       │
│       varchar        │       varchar        │     varchar     │   │       varchar        │      double       │       varchar       │
├──────────────────────┼──────────────────────┼─────────────────┼───┼──────────────────────┼───────────────────┼─────────────────────┤
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ AP                   │ 1726394702721.481 │ media-playout       │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CF9A:6C:31:80:50:F…  │ 1726394702721.481 │ certificate         │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CFAF:51:8E:09:37:2…  │ 1726394702721.481 │ certificate         │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ COTdata1_109_maxpl…  │ 1726394702721.481 │ codec               │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ COTdata1_120_profi…  │ 1726394702721.481 │ codec               │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CP/NH8cQqe_eL6zYNON  │ 1726394702721.481 │ candidate-pair      │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CP08b8N49i_eL6zYNON  │ 1726394702721.481 │ candidate-pair      │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CPBDwwCTaU_eL6zYNON  │ 1726394702721.481 │ candidate-pair      │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CPYLu975lS_eL6zYNON  │ 1726394702721.481 │ candidate-pair      │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CPki/8xp1m_eL6zYNON  │ 1726394702721.481 │ candidate-pair      │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ CPki/8xp1m_eYTJlek6  │ 1726394702721.481 │ candidate-pair      │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ D5                   │ 1726394702721.481 │ data-channel        │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ D6                   │ 1726394702721.481 │ data-channel        │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ D7                   │ 1726394702721.481 │ data-channel        │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ D8                   │ 1726394702721.481 │ data-channel        │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ I/NH8cQqe            │ 1726394702721.481 │ local-candidate     │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ I08b8N49i            │ 1726394702721.481 │ local-candidate     │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ I4uDdiSuP            │ 1726394702721.481 │ local-candidate     │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ IBDwwCTaU            │ 1726394702721.481 │ local-candidate     │
│ F6WJ4SY2HD63Z25XD3…  │ DE5MC2JG3H2PK667ZG…  │ WebRTC SFU Sora │ … │ IT0OYEKLy            │ 1726394702721.481 │ local-candidate     │
│          ·           │          ·           │        ·        │ · │     ·                │         ·         │       ·             │
│          ·           │          ·           │        ·        │ · │     ·                │         ·         │       ·             │
│          ·           │          ·           │        ·        │ · │     ·                │         ·         │       ·             │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ CPp2HkMADY_vKxy9BYC  │ 1726403015487.149 │ candidate-pair      │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ D5                   │ 1726403015487.149 │ data-channel        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ D6                   │ 1726403015487.149 │ data-channel        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ D7                   │ 1726403015487.149 │ data-channel        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ D8                   │ 1726403015487.149 │ data-channel        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ITdata1A2376627921   │ 1726403015487.149 │ inbound-rtp         │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ITdata1A3686590866   │ 1726403015487.149 │ inbound-rtp         │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ITdata1V3657862824   │ 1726403015487.149 │ inbound-rtp         │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ITdata1V494618204    │ 1726403015487.149 │ inbound-rtp         │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ OTdata1A3589631305   │ 1726403015487.149 │ outbound-rtp        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ OTdata1V886471106    │ 1726403015487.149 │ outbound-rtp        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ RIA3589631305        │   1726403011612.0 │ remote-inbound-rtp  │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ RIV886471106         │   1726403014647.0 │ remote-inbound-rtp  │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ROA2376627921        │   1726403013580.0 │ remote-outbound-rtp │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ROA3686590866        │   1726403011612.0 │ remote-outbound-rtp │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ROV3657862824        │   1726403015068.0 │ remote-outbound-rtp │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ ROV494618204         │   1726403014750.0 │ remote-outbound-rtp │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ SA3                  │ 1726403015487.149 │ media-source        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ SV4                  │ 1726403015487.149 │ media-source        │
│ ZVWETDA641527D2A6T…  │ S31C88V2SX7M76DD6M…  │ WebRTC SFU Sora │ … │ Tdata1               │ 1726403015487.149 │ transport           │
├──────────────────────┴──────────────────────┴─────────────────┴───┴──────────────────────┴───────────────────┴─────────────────────┤
│ 83911 rows (40 shown)                                                                                         20 columns (6 shown) │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Parquetのデータをインポートし、S3互換APIで読み出して、さらにDuckDBのSQLを使って分析ができることが確認できた。

## Python経由でcsvデータを読むのにDuckDBが使えるか確認する
今度はPythonのDuckDBライブラリを使ってローカルのcsvを直接分析できるかを確認する。なお、Python経由で使う場合はDuckDBはライブラリの中に含まれているため、ローカルにインストールする必要はない。

以下を実行する。

```bash
uv sync
make run
```

ローカルのcsvにSQLをかけた結果が返ってくることが確認できた。

```bash
uv run python src/main.py
┌─────────┬─────────┬──────────────────────┬─────────────────┬───┬─────────┬───────────┬──────────────────────┬──────────────────────┐
│ show_id │  type   │        title         │    director     │ … │ rating  │ duration  │      listed_in       │     description      │
│ varchar │ varchar │       varchar        │     varchar     │   │ varchar │  varchar  │       varchar        │       varchar        │
├─────────┼─────────┼──────────────────────┼─────────────────┼───┼─────────┼───────────┼──────────────────────┼──────────────────────┤
│ s1      │ Movie   │ Dick Johnson Is Dead │ Kirsten Johnson │ … │ PG-13   │ 90 min    │ Documentaries        │ As her father near…  │
│ s2      │ TV Show │ Blood & Water        │ NULL            │ … │ TV-MA   │ 2 Seasons │ International TV S…  │ After crossing pat…  │
│ s3      │ TV Show │ Ganglands            │ Julien Leclercq │ … │ TV-MA   │ 1 Season  │ Crime TV Shows, In…  │ To protect his fam…  │
│ s4      │ TV Show │ Jailbirds New Orle…  │ NULL            │ … │ TV-MA   │ 1 Season  │ Docuseries, Realit…  │ Feuds, flirtations…  │
│ s5      │ TV Show │ Kota Factory         │ NULL            │ … │ TV-MA   │ 2 Seasons │ International TV S…  │ In a city of coach…  │
├─────────┴─────────┴──────────────────────┴─────────────────┴───┴─────────┴───────────┴──────────────────────┴──────────────────────┤
│ 5 rows                                                                                                        12 columns (8 shown) │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────┬─────────────────────┬─────────────────────┬───┬─────────────────────┬─────────────────────┬────────────┐
│        date         │        open         │        high         │ … │        close        │      adj_close      │   volume   │
│      timestamp      │       double        │       double        │   │       double        │       double        │   int64    │
├─────────────────────┼─────────────────────┼─────────────────────┼───┼─────────────────────┼─────────────────────┼────────────┤
│ 1997-05-15 04:00:00 │ 0.12187500298023224 │               0.125 │ … │ 0.09791699796915054 │ 0.09791699796915054 │ 1443120000 │
│ 1997-05-16 04:00:00 │ 0.09843800216913223 │ 0.09895800054073334 │ … │  0.0864579975605011 │  0.0864579975605011 │  294000000 │
│ 1997-05-19 04:00:00 │ 0.08802100270986557 │ 0.08854199945926666 │ … │  0.0854170024394989 │  0.0854170024394989 │  122136000 │
│ 1997-05-20 04:00:00 │  0.0864579975605011 │ 0.08749999850988388 │ … │ 0.08177100121974945 │ 0.08177100121974945 │  109344000 │
│ 1997-05-21 04:00:00 │ 0.08177100121974945 │ 0.08229199796915054 │ … │ 0.07135400176048279 │ 0.07135400176048279 │  377064000 │
├─────────────────────┴─────────────────────┴─────────────────────┴───┴─────────────────────┴─────────────────────┴────────────┤
│ 5 rows                                                                                                   7 columns (6 shown) │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## MinIOに保存したファイルをパブリックに公開する方法
GUIから操作する場合、バケット単位でPublicに設定する場合はバケットの設定からPublicのトグルをONにした上で、ブラウザから `http://<IP:ポート（docker-composeの設定では9000）>/<パス>/<ファイル名>` にアクセスすればよい。URLの対応は以下:

| 画面 | URL |
| --- | --- |
| 管理画面 | http://localhost:9001/browser/duckdb-local/spam.parquet |
| 対応する公開URL | http://localhost:9000/duckdb-local/spam.parquet |

## Sample Data
- [netflix_titles.csv](https://www.kaggle.com/datasets/anandshaw2001/netflix-movies-and-tv-shows?resource=download)

## 参考
- https://zenn.dev/shiguredo/articles/duckdb-minio