<p align="center">
    <h1>Horoscofox Service 🦄 🌈</h1>
    <br>
     
</p>

## Start 💫
Visit demo at [https://horoscofox.github.io](https://horoscofox.github.io)

### Start without docker
We use [Pipenv](https://github.com/pypa/pipenv) to manage dependencies

    pip install pipenv
    cd horoscofox-service
    pipenv install 

<!-- 
### Start with docker 🐳
*(we **strongly** recommend this way)*

    docker-compose build
    docker-compose up
-->


## APIs 🌍
`<astrologer> / <sign> / <kind>`

### Parameters
**Astrologers** allowed are 

`paolo`  `branko`  `fox`  `paolofox`

**Signs** allowed are 

`capricorn`  `aquarius`  `pisces`  `aries`  `taurus`  `gemini`  `cancer`  `leo`  `virgo`  `libra`  `scorpio`  `sagittarius`

**Kinds** allowed *(at the moment)* are 

`today` `tomorrow`

## Tests 🐲
<!--
**Using docker**

    docker-compose run backend bash
    . runtest.sh
-->
**Without docker**

    . runtest.sh

---

#### For further information
[pyhoroscofox](https://github.com/horoscofox/pyhoroscofox "pyhoroscofox"):  Python horoscope library

[Dynamo DB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html "Dynamo DB"):  Setup DynamoDB locally

[Zappa on Docker](https://blog.zappa.io/posts/docker-zappa-and-python3 "Zappa"):  Allows you to have a local environment that can be used to debug package

---
### License
Service used in this project are under these licence


| Service            | Licence                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------|
| Zappa              | [MIT](https://github.com/Miserlou/Zappa/blob/master/LICENSE)                                |
| Apistar            | [BSD-3-Clause](https://github.com/encode/apistar/blob/master/LICENSE.md)                    |
| Boto3              | [Apache 2.0](https://github.com/boto/boto3/blob/develop/LICENSE)                            |
| Apistar Cors Hooks | [BSD 3-Clause](https://github.com/lucianoratamero/apistar_cors_hooks/blob/master/LICENSE)   |
| Pyhoroscofox       | [MIT](https://github.com/horoscofox/pyhoroscofox/blob/master/LICENSE)                       |
