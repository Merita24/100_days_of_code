def json_to_table(func):
    def wrapper(*args, **kwargs):
        data = list(func(*args, **kwargs))  # convert generator → list

        if not data:
            return []

        headers = list(data[0].keys())
        rows = [headers]

        for item in data:
            rows.append([item.get(h) for h in headers])

        return rows

    return wrapper


@json_to_table
def user_stream():
  yield{'id':1,"name":"Alice"}
  yield{"id":2,"name":"Bob"}
  yield{"id":3,"name":"Paul"}


stream1=user_stream()

for row in stream1:
    print(row)