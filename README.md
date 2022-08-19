# 불법주정차 통합 지도 서비스

github: https://github.com/robert-min/daegu-parking
period: 2022년 1월 30일 → 2022년 2월 10일
project: 공모전
tech: CSS, Flask, Javascript, MySQL, PHP

## Preview

![스크린샷 2022-02-11 오후 3.39.58.png](%E1%84%87%E1%85%AE%E1%86%AF%E1%84%87%E1%85%A5%E1%86%B8%E1%84%8C%E1%85%AE%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%8E%E1%85%A1%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B8%20%E1%84%8C%E1%85%B5%E1%84%83%E1%85%A9%20%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3%20541d639d07054b03aa115d8c36430c18/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-02-11_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.39.58.png)

[Robert-DEV-Blog](https://www.notion.so/652b5c946354470ca13ebec98df7b39d)

## 공공데이터 개발활용 가속화 해커톤

### 해커톤 내용

행정안전부와 한국지능정보사회진흥원(NIA)에서는 디지털 뉴딜 사업의 일환으로 공공데이터 개방‧활용 가속화를 위해 『공공데이터 기업 매칭 지원사업』을 추진하고 있습니다. 기업 매칭으로 구축‧개방된 데이터의 이용 활성화와 추가적으로 개방이 필요한 데이터 발굴 및 확산을 위해 “공공데이터 개발‧활용 가속화 해커톤”을 아래와 같이 개최하오니 많은 관심과 참여를 바랍니다.

### 해커톤 과제

- (공모부문) 공공데이터 활용 아이디어 기획, 서비스 개발(프로토타입)
    - 공공데이터 포털([www.data.go.kr](http://www.data.go.kr/))에 개방된 데이터 및 API를 활용한 아이디어 기획 및 서비스 개발
- (필수조건) 공공데이터 기업 매칭 지원사업의 개방데이터* 30% 이상 활용, 추가 개방이 필요한 공공데이터 제시 필수

### 파일 목록 - **불법주정차 민원 감소를 위한 데이터 DB 구축 및 OpenAPI 개발**

| 파일명 | 링크 | 데이터 수 |
| --- | --- | --- |
| 대구광역시 북구_불법주정차 민원 | https://www.data.go.kr/data/15096495/fileData.do | 14814 |
| 대구광역시 북구_불법주정차 민원 현장 정보(상습지역) | https://www.data.go.kr/data/15096498/fileData.do | 142 |
| 대구광역시 북구_공영주차장 운영 현황 및 현장 정보 | https://www.data.go.kr/data/15096499/fileData.do | 229 |
| 대구광역시 북구_민영주차장 운영 현황 및 현장 정보 | https://www.data.go.kr/data/15096532/fileData.do | 35 |
| 대구광역시 북구_노상주차장 운영 현황 및 현장 정보 | https://www.data.go.kr/data/15096533/fileData.do | 179 |
| 대구광역시 북구_개방공유 주차장 현황 | https://www.data.go.kr/data/15096534/fileData.do | 5 |
| 대구광역시 북구_노인장애인보호구역 현황 | https://www.data.go.kr/data/15096535/fileData.do | 118 |
| 대구광역시 북구_보행자 전용도로 현황 | https://www.data.go.kr/data/15096537/fileData.do | 120 |

## Project : 불법주정차 통합 지도 서비스

### 서비스 개요

불법주정차는 해당 지역 거주자와 보행자의 안전과 매우 큰 관련이 있어 이를 해결하는 것은 매우 중요한 일입니다.  하지만 현재 이를 해결하기위해 주기적인 주정차 단속을 제외한 뚜렷한 해결책이 없는 상황이고, 이로 인해 불법주정차와 관련된 민원은 점점 증가한 상황입니다. 이러한 불법주정차 문제의 원인은 불법주정차에 대한 정보가 운전자에게 제대로 전달되지 못하고 있는 점입니다.

이를 해결하기 위해 불법주정차 통합 지도 서비스를 제공합니다. 지도api를 활용해 불법주정차 민원 지역과 노인장애인보호구역 보행자 전용도로 등의 주정차가 불가능한 지역의 정보 제공과 주차가 가능한 공영 민영 주차장 정보를 제공하여 불법주정차 민원 감소에 기여하는 서비스입니다.

### 서비스 기능

1. 불법주정차 민원 정보를 통합적으로 관리할 수 있는 DB 생성 & 불법주정차 민원 위치 정보 지도에 마커 형태로 표시 및 관련 정보 제공
2. 노인장애인보호구역 및 어린이 보호구역 위치 정보 지도에 반경 300m 주정차 금지 정보 제공
3. 공명, 민영, 노상, 개방 주차장 통합적으로 관리할 수 있는 DB 생성 & 주차장 위치 정보 도에 마커 형태로 표시 및 관련 정보 제공

## 서비스 개발 핵심 정리

### csv 파일 확인 후 MySQL에 데이터 저장

- [공공데이터포털](https://www.data.go.kr/index.do) 사이트에서 직접 데이터 호출 가능하지만 회원가입과 승인하는 단계가 필요하기 때문에 이번 프로젝트에서는 csv 파일을 다운받고 불러오는 방법으로 진행
- 데이터를 확인하고 다루는 방법이 많지만 그 중, Pandas를 사용하여 전처리 작업과 저장하는 작업 진행 → 불법주정차, 주차장, 노인장애인보호구역 데이터 모두 저장하는 방법 동일

```python
# illegal_parking.ipynb 
# 라이브러리 로드
import pandas as pd
import pymysql

# 파일 로드 -> encoding을 해야 파일을 깨지지 않고 확인할 수 있음
df_il_parking = pd.read_csv("ori_file/대구광역시 북구_불법주정차 민원_20211123.csv", encoding="cp949")

# 데이터 확인
df_il_parking.describe()

# 결측치 확인
df_il_parking.isnull().value_counts()
```

- 데이터를 확인해보면 동일한 지역 동일한 해에 데이터가 따로 입력되어 있는 것을 확인할 수 있음.
- 중복되어 있는 값을 따른 DataFrame으로 분리한 후 데이터를 합친 다음 기존 DataFrame에 합치는 전처리 과정 진행

```python
# illegal_parking.ipynb 
# 중복되어 있는 값만 따로 DataFrame으로 분리(중복되어 있는 값 True)
df_test = df_il_parking[df_il_parking.duplicated(["주소", "민원발생년도"], keep=False) == True]

# 분리된 DataFrame에서 중복되어 있는 값 민원발생누적건수로 합치기
df_il_dup = df_test.groupby(["주소", "민원발생년도"])["민원발생누적건수"].sum().reset_index()
# 반복문으로 데이터를 입력할 수 있게 해당 데이터 리스트와 딕셔너리 형태로 각각 분리
dup_address = df_il_dup["주소"].tolist()
dup_dict = df_il_dup.to_dict('index')

# 원본데이터에서 중복된 데이터 중 하나만 남기기
df = df_il_parking.drop_duplicates(["주소", "민원발생년도"])

# 데이터 입력
for i, address in enumerate(dup_address):
    df.loc[df["주소"] == address, "민원발생누적건수"] = dup_dict[i]["민원발생누적건수"]

# 데이터 확인
df.head()
```

- MySQL에 db 생성 후 table 생성

```python
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='[패스워드]',
    db='[DB명]',
    charset='utf8'
)

cursor = db.cursor()

sql = """
    CREATE TABLE illegal (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        address VARCHAR(40) NOT NULL,
        count INT UNSIGNED NOT NULL,
        year INT UNSIGNED NOT NULL,
        lat FLOAT NOT NULL,
        lng FLOAT NOT NULL,
        PRIMARY KEY(id));
"""

cursor.execute(sql)

db.commit()

db.close()
```

- Table에 데이터 입력

```python
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='[패스워드]',
    db='[DB명]',
    charset='utf8'
)

try:
    cursor = db.cursor()

    for num in range(14678):
        sql = "INSERT IGNORE INTO illegal VALUES ({0}, '{1}', {2}, {3}, {4}, {5});".format(
            str(num),  # autoincrement를 table 생성할 때 설정했기 때문에 안넣어도 됨!!
            df.loc[num, "주소"],
            int(df.loc[num, "민원발생누적건수"]),
            df.loc[num, "민원발생년도"],
            df.loc[num, "경도"],
            df.loc[num, "위도"])
        print(sql)
        cursor.execute(sql)

    db.commit()
finally:
    db.close()
```

- DB 확인

![스크린샷 2022-02-11 오후 5.05.23.png](%E1%84%87%E1%85%AE%E1%86%AF%E1%84%87%E1%85%A5%E1%86%B8%E1%84%8C%E1%85%AE%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%8E%E1%85%A1%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B8%20%E1%84%8C%E1%85%B5%E1%84%83%E1%85%A9%20%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3%20541d639d07054b03aa115d8c36430c18/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-02-11_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.05.23.png)

### DB와 html 통신을 위한 PHP 파일 생성

- 처음 DB에 있는 데이터를 html 지도에 올리기위해 Flask pymysql을 통해 연결하는 방법으로 진행 함. → 결과적으로는 실패...!! → 여러 정보를 찾아서 연동까지는 성공 했지만 몇 만건의 데이터를 Flask를 거쳐서 html에 전달하는 것이 불가능함을 확인(이 때, 처음으로 Serverside-Script인 PHP에대해 알게 됨!!)
- PHP를 초기 개발환경에 세팅하는 과정이 매우 힘듬 → 이 블로그 많은 도움이 됨!! [https://tech.10000lab.xyz/php/php-apache-part1.html](https://tech.10000lab.xyz/php/php-apache-part1.html)

```php
// getNonParking.php
<?php
    header("Content-Type:application/json");
    header("Access-Control-Allow-Origin: *");

    // 1. 데이터베이스에서 데이터를 가져옴
    $link = mysqli_connect("localhost", "root", "[비밀번호]", "[DB명]");
    if ($result = mysqli_query($link, 'SELECT * FROM `illegal` WHERE count >= 100;', MYSQLI_USE_RESULT)) {
        // 2. 데이터베이스로부터 반환된 데이터를
        // 객체 형태로 가공함
        $o = array();
        while ($row = mysqli_fetch_object($result)) {
            $t = new stdClass();
            $t->id = $row->id;
            $t->address = $row->address;
            $t->count = $row->count;
            $t->year = $row->year;
            $t->lat = $row->lat;
            $t->lng = $row->lng;
            $o[] = $t;
            unset($t);
        }
    } else {
        $o = array( 0 => 'empty');
    }

    // 3, 4 최종 결과 데이터를 JSON 스트링으로 변환 후 출력
    echo json_encode($o);
```

### 카카오 지도 api를 활용해 원하는 형태의 html 구성

- [https://apis.map.kakao.com/](https://apis.map.kakao.com/)
- 카카오 개발자 사이트에서 회원가입 후 apikey 생성
- 해당 홈페이지의 Docs와 Example 내용을 통해 내가 구현하고자하는 기능 구현 → Document를 자세하게 읽어보면 어떻게 코드를 구성해봐야할지 알 수 있음
- jquery ajax를 활용해 데이터를 가져와서 마커 구현

```jsx
var illegal_markers = [];

    function setIllegalMarkers() {
        console.log("illegal")
        $.ajax({
            type: 'post',
            dataType: 'json',
            url: 'http://localhost/PycharmProjects/Deagu_parking/templates/getNonParking.php',
            success: function (positions) {
                // 마커 이미지의 이미지 주소입니다
                var imageSrc = "http://localhost/PycharmProjects/Deagu_parking/templates/img/nonparking.png";
                for (var i = 0; i < positions.length; i++) {

                    // 마커 이미지의 이미지 크기 입니다
                    var imageSize = new kakao.maps.Size(18, 18);

                    // 마커 이미지를 생성합니다
                    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

                    var latlng = new kakao.maps.LatLng(positions[i].lat, positions[i].lng)

                    // 마커를 생성합니다
                    var marker = new kakao.maps.Marker({
                        map: map, // 마커를 표시할 지도
                        position: latlng, // 마커를 표시할 위치
                        image: markerImage
                    });

                    illegal_markers.push(marker);

                    // var iwContent = '<div style="padding:5px; width:100%;">' + positions[i].address + "<br>" + positions[i].count + "</br>" + '</div>'; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
                    var content = '<div class="overlaybox">' +
                        '    <div class="boxtitle">' + positions[i].address + '</div>' +
                        '    <div class="first">' +
                        '    </div>' +
                        '    <ul>' +
                        '        <li class="up", align="right">' +
                        '            <span class="number">' + positions[i].count + '</span>' +
                        '            <span class="title">건</span>' +
                        '        </li>' +
                        '    </ul>' +
                        '</div>';

                    var customOverlay = new kakao.maps.CustomOverlay({
                        position: latlng,
                        content: content,
                        xAnchor: 0.32,
                        yAnchor: 0.58
                    });

                    // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
                    // 이벤트 리스너로는 클로저를 만들어 등록합니다
                    // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
                    kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, customOverlay));
                    kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(customOverlay));
                    kakao.maps.event.addListener(map, 'click', makeOutListener(customOverlay));
                }
            }
        });

    }
```

- 원하는 형태로 구현되었는지 확인

![Untitled](%E1%84%87%E1%85%AE%E1%86%AF%E1%84%87%E1%85%A5%E1%86%B8%E1%84%8C%E1%85%AE%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%8E%E1%85%A1%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B8%20%E1%84%8C%E1%85%B5%E1%84%83%E1%85%A9%20%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3%20541d639d07054b03aa115d8c36430c18/Untitled.png)

![Untitled](%E1%84%87%E1%85%AE%E1%86%AF%E1%84%87%E1%85%A5%E1%86%B8%E1%84%8C%E1%85%AE%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%8E%E1%85%A1%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B8%20%E1%84%8C%E1%85%B5%E1%84%83%E1%85%A9%20%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3%20541d639d07054b03aa115d8c36430c18/Untitled%201.png)

### Project 회고

개발자로 참여하는 첫번째 프로젝트를 처음에 목표로 했던 기간내에 완료할 수 있어서 다행. 특히 프론트쪽 지식이 하나도 없는 상태에서 진행하다보니 중간에 헤매는 시간이 많았지만 그만큼 많은 것을 배울 수 있어서 좋았음데이터 엔지니어를 목표로하고 있지만 기본적인 개발 지식은 필수이기 때문에 이번 웹서비스 프로젝트와 2월 중순에 추가로 진행해볼 앱 프로젝트를 통해 개발 역량을 높이는데 집중!!