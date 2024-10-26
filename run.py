from redis_om import HashModel, JsonModel, get_redis_connection


class SampleData(JsonModel):
    title: str
    code: int


class User(HashModel):
    name: str
    mail: str


def main():
    # francois = User(name="François", mail="françois@mail.com")
    data_sample = SampleData(title="document 1", code=89)
    data_sample.save()
    print(data_sample)

if __name__ == "__main__":
    main()
