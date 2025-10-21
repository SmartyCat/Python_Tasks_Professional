def sourcetemplate(url):
    def func(**kwargs):
        if kwargs:
            return (
                url + "?" + "&".join(sorted(k + "=" + str(kwargs[k]) for k in kwargs))
            )
        return url

    return func


url = "https://beegeek.ru"
load = sourcetemplate(url)
print(load(name="timur"))

url = "https://stepik.org/lesson/651459/step/14"
load = sourcetemplate(url)
print(load(thread="solutions", unit=648165))
url = "https://beegeek.ru"
load = sourcetemplate(url)
print(load())
