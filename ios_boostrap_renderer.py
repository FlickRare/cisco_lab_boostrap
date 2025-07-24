from jinja2 import Environment, FileSystemLoader

hosts = [
    {"hostname": "D1", "ip_address": "192.168.42.2"},
    {"hostname": "D2", "ip_address": "192.168.42.3"},
    {"hostname": "D3", "ip_address": "192.168.42.4"},
    {"hostname": "A1", "ip_address": "192.168.42.5"},
    {"hostname": "A2", "ip_address": "192.168.42.6"},
    {"hostname": "A3", "ip_address": "192.168.42.7"},
    {"hostname": "A4", "ip_address": "192.168.42.8"},
    {"hostname": "A5", "ip_address": "192.168.42.9"},
    {"hostname": "A6", "ip_address": "192.168.42.10"},
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("AccessSW-BS-template.j2")

for host in hosts:
    FILENAME = f"{host["hostname"]}_boostrap.ios"
    content = template.render(host)
    
    with open(FILENAME, mode="w", encoding="utf-8") as boostrap_script:
        boostrap_script.write(content)
        print(f"Generated {host["hostname"]} config.")
        