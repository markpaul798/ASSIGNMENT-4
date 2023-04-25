Def validate(ip):
    # Split the input string by period delimiter
    Octets = ip.split(“.”)

    # Check if the input string contains exactly 4 octets
    If len(octets) != 4:
        Return False

    # Check if each octet is a valid integer in the range [0, 255]
    For octet in octets:
        If not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            Return False

    Return True
