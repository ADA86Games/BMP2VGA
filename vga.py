from argparse import ArgumentParser


def convert_vga(file_name: str) -> None:
    """
    Open a BMP file and convert it into a
        VGA data file.

    :param file_name: The file name of the bmp file.
    """
    bmp_data = []
    with open(file_name, "rb") as bmp_file:
        bmp_data = bmp_file.read()
    vga_pointer = bmp_data[10] # This is the flag in BMP header
    # holding location of Pixel Data.
    vga_data = bmp_data[vga_pointer:vga_pointer + 320 * 200]
    with open(file_name.replace(".bmp", ".vga"), "wb") as output:
        output.write(vga_data)


if __name__ == '__main__':
    parser = ArgumentParser(prog="BMP2VGA Converter",
                            description="Convert a BMP file to a VGA data file.")
    parser.add_argument("--file", action="store", help="The name of the BMP file")
    args = parser.parse_args()
    convert_vga(args.file)

