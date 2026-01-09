from hydrotoolbox import bfi_from_rdb


def main():
    bfi_from_rdb(
        input_path=R".\bfi_example\NWIS_discharge_02203655.rdb",
        output_dir=R".\Output",
    )


if __name__ == "__main__":
    main()
