import subprocess


def docker_run():
    cmd = f'docker run -d --name docker_theia3000 -p 3000:3000 -v "$(pwd):/home/project:cached" elswork/theia'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0].decode("utf-8")[:-1]
    print(result)
    return result


def docker_remove(id):
    cmd = f'docker rm -f {id}'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0].decode("utf-8")[:-1]
    print(result)
    return result
