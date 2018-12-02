import time


def case(*args, **kwargs):
    result_dict = {}
    if "tags" in kwargs:
        for tag in kwargs["tags"]:
            result_dict[tag] = kwargs["tags"][tag]

    if "setup" in kwargs:
        setup = kwargs["setup"]

    if "teardown" in kwargs:
        teardown = kwargs["teardown"]

    def case_decorator(fun):
        def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                setup()
                fun(*args, **kwargs)
                result = "Pass"
            except AssertionError, msg:
                result_dict["exception_msg"] = msg
                result = "Fail"
            except Exception, msg:
                result_dict["exception_msg"] = msg
                result = "Error"
            finally:
                teardown()

            end_time = time.time()
            result_dict["result"] = result
            result_dict["run_time"] = end_time - start_time

            print result_dict
        return wrapper
    return case_decorator


