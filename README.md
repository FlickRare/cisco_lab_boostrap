# Cisco Lab Bootstrap

Quickly generate initial configurations with jinja to enable Cisco IOS SSH access in virtual lab environments.

## File Structure

```
.
├── ios_boostrap_renderer.py
└── templates/
    └── AccessSW-BS-template.j2
```

## Usage

1. Install dependencies ```python3 -m pip install -r requirements.txt```
2. Modify templates in `templates/` as needed, avoid text wrapped in {{ curly brackets}} unless you know what you're doing.
3. Run `ios_boostrap_renderer.py` to generate configurations
4. Apply generated configs to virtual Cisco devices

For detailed instructions, see comments in `cisco_lab_bootstrap.py`.