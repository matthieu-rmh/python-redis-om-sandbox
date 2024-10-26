from redis_om import HashModel, JsonModel, get_redis_connection

redis_conn = get_redis_connection(url="redis://localhost:6379")

class SampleData(JsonModel):
    title: str
    code: int
    class Meta:
        database=redis_conn


class User(HashModel):
    name: str
    mail: str

def main():
    francois = User(name="François", mail="françois@mail.com")
    # data_sample = SampleData(title="document 1", code=89)
    # data_sample.save()
    print(francois)

if __name__ == "__main__":
    main()
