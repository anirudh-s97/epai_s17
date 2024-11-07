def run_job(data, template, check, error):
    for key in template:
        if not isinstance(template[key], dict):
            if key not in data:
                check = False 
                error[key] = "missing"
                break

            elif not isinstance(data[key], template[key]):
                check = False
                error[key] = "bad"
                break

        else:

            if data.get(key) is not None:
                
                data_keys = set(data[key].keys())
                template_keys = set(template[key].keys())
                
                if (template_keys | data_keys) != template_keys:
                    check = False
                    extra_key = list(data_keys.difference(template_keys))[0]
                    error[extra_key] = "missing"
                    error[key] = 1
                    break

                else:
                    check, error = run_job(data[key], template[key], check, error)
                    if error != {}:
                        error[key] = 1
                        break
                    else:
                        continue
            else:
                check = False
                break

    return check, error
    

def validate(data, template):
    try:
        check = True
        error = {}
        check, error = run_job(data, template, check, error)
        if check:
            error = ''
        else:
            error_str = list(error.keys())
            error_str.reverse()
            error_str = ".".join(error_str)

            if "missing" in list(error.values()):
                print("values", error.values())
                error = "mismatched keys: {}".format(error_str)
            else:
                error = "bad type: {}".format(error_str)
        print("actual_error", error)
        return check, error
    
    except Exception as e:
        print(e)

