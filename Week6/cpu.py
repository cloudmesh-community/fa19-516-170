from flask import jsonify
import cpuinfo


def get_processor_name():
    p = cpuinfo.get_cpu_info()['brand']
    pinfo = {"model": p}
    return jsonify(pinfo)


def get_processor_cache(level):
    if level == "l2":
        p2 = cpuinfo.get_cpu_info()['l2_cache_size']
        p2info = {"l2": p2}
        return jsonify(p2info)
    elif level == "l3":
        p3 = cpuinfo.get_cpu_info()['l3_cache_size']
        p3info = {"l3": p3}
        return jsonify(p3info)
    else:
        cache_info = {}
        cache_info["l2"] = cpuinfo.get_cpu_info()['l2_cache_size']
        cache_info["l3"] = cpuinfo.get_cpu_info()['l3_cache_size']
        return jsonify({"caches": cache_info})
