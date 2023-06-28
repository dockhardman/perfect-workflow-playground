from prefect import flow, task


@task
def say_hello(name):
    return f"Hello {name}!"


@task
def print_result(result):
    print(type(result))  # <class 'str'>
    print(result)  # Hello Marvin!


@flow(name="hello-flow")
def hello_world():
    future = say_hello.submit("Marvin")
    print(type(future))  # <class 'prefect.futures.PrefectFuture'>
    print_result.submit(future)


hello_world()
