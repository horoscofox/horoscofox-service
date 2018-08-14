import .dynamongorm as orm


class Horoscope(dynamongorm.Model):
    text = orm.StringField(
        max_length=None, min_length=None, required=True)
    sign = orm.StringField(max_length=15, required=True)
    astrologer = orm.AstrologerField(
        max_length=3, required=True, choices=ASTROLOGER_UID)
