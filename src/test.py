import download


if __name__ == "__main__":
    with open('../resource/index.html', 'rb') as foo_file:
        result = download.spiderDown(foo_file, 'test')
