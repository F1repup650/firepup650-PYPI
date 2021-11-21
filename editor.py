def edit():
# Edit setup.cfg
  my_file = open("package/setup.cfg")
  string_list = my_file.readlines()
  my_file.close()
  ver = input("Version: ")
  update = input("What's new?: ")
  string_list[2] = f"version = {ver}\n"
  my_file = open("package/setup.cfg", "w")
  new_file_contents = "".join(string_list)
  my_file.write(new_file_contents)
  my_file.close()
# Edit README.md
  my_file = open("package/README.md")
  string_list = my_file.readlines()
  my_file.close()
  string_list[9] = f"###### v.{ver}:\n"
  string_list[10] = f"{update}\n"
  my_file = open("package/README.md", "w")
  new_file_contents = "".join(string_list)
  my_file.write(new_file_contents)
  my_file.close()