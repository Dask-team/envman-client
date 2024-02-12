# envman-client

### To-do

- [ ] `init` 만들기
    - 기본적으로 envmanifest.json 파일을 생성하고, 그 안에 기본적인 설정을 넣는다. (어떤 스테이지가 있는지, sqlite db 이름이 뭔지 등)
    - 만약 이미 envmanifest.json 파일이 있다면, 덮어쓸지 물어본다. (덮어쓰는 경우 기존 db, env 등 파일 싹 날린다)
    - 기본적으로 common 스테이지를 만들고, 이를 .env에 대응한다.
    - sqlite db에 env, log, stage 테이블을 만든다.
    - .env 파일을 만든다.
    - .gitignore에 .env를 추가한다.
    - .env 파일에는 기본적으로 common 스테이지를 가리키도록 한다.

```
python envman.py init
python envman.py init --envfile environ
python envman.py init --db envman
python envman.py init --envfile environ --db envman
```

- [ ] `add` 만들기
    - 그냥 python envman.py add AWS_SECRET_KEY 1234 --stage dev 이런 식으로 하면, dev 스테이지에 AWS SECRET KEY가 1234로 추가된다.
    - 만약 --stage 옵션이 없으면, common 스테이지에 추가된다.
    - 만약 --stage 옵션이 없는데, common 스테이지에 이미 같은 이름의 env가 있다면, 덮어쓸지 물어본다.
    - 만약 --stage 옵션이 있는데, 이미 같은 이름의 env가 있다면, 덮어쓸지 물어본다.
    - 만약 --stage 옵션이 있는데, 같은 이름의 env가 없다면, 추가한다.

```
python envman.py add AWS_SECRET_KEY 1234
python envman.py add AWS_SECRET_KEY 1234 --stage dev
python envman.py add AWS_SECRET_KEY 1234 --stage all
```

- [ ] `remove` 만들기
    - 그냥 python envman.py remove AWS_SECRET_KEY --stage dev 이런 식으로 하면, dev 스테이지에 AWS SECRET KEY가 삭제된다.
    - 만약 --stage 옵션이 없으면, common 스테이지에서 삭제된다.
    - 만약 --stage 옵션이 없는데, common 스테이지에 해당 env가 없다면, 에러를 띄운다.
    - 만약 --stage 옵션이 있는데, 해당 스테이지에 해당 env가 없다면, 에러를 띄운다.

- [ ] `list` 만들기

- [ ] `gitignore` 만들기
    - .gitignore에 .env와 stage별 env 파일들을 추가한다. (예를 들어, .env.dev, .env.prod 등)
    - .gitignore에 envmanifest.json 및 sqlite db 등의 파일도 추가한다.
    - 이미 동일한 이름의 파일이 있다면, 추가하지 않는다.

- [ ] `pull` 만들기
    - 서버 주소와 포트, 그리고 인증 정보를 받아서, 해당 서버로부터 db 로그를 받아온다.
    - 받아온 db 로그를 sqlite db에 적용한다.
    - 서로 다른 env 내용이 있는 경우, 각 환경변수별로 사용자에게 어떻게 할지 물어본다.
    - 인수로 --force로 받는 경우에 한해서, 사용자에게 물어보지 않고 무조건 서버 파일로 덮어쓴다.
    - --latest 옵션을 받으면, 가장 최근에 반영된 환경변수로 모든걸 세팅한다.

- [ ] `push` 만들기
    - 서버 주소와 포트, 그리고 인증 정보를 받아서, 해당 서버로 envmanifest.json 파일을 전송한다.
    - 
