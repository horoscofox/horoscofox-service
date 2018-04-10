<p align="center">
    <h1>Horoscofox Service 🦄 🌈</h1>
    <br>
</p>

## Start 💫

### Start without docker
We use [Pipenv](https://github.com/pypa/pipenv) to manage dependencies

    pip install pipenv
    cd horoscofox-service
    pipenv install 

Install MongoDB on your machine [see official docs](https://docs.mongodb.com/manual/administration/install-community/)

Setup your Mongo connection in `horoscofox-service/settings.py`

### Start with docker 🐳
*(we **strongly** recommend this way)*

    docker-compose build
    docker-compose up



## APIs 🌍
`<astrologer> / <sign> / <kind>`

### Parameters
**Astrologers** allowed are 

`paolo`  `branko`  `fox`  `paolofox`

**Signs** allowed are 

`capricorn`  `acquarius`  `pisces`  `aries`  `taurus`  `gemini`  `cancer`  `leo`  `virgo`  `libra`  `scorpio`  `sagittarius`

**Kinds** allowed *(at the moment)* are 

`today` `tomorrow`

---

#### For further information
[pyhoroscofox](https://github.com/horoscofox/pyhoroscofox "pyhoroscofox"):  Python horoscope library