# <!-- Day Card -->
# <label for="" class="day-card">
# <input type="checkbox" >
# <span></span>
# </label>

text = ""
count = 0
for i in range(28, 32):
  count += 1
  text += f"""\n<!-- Day {str(count).zfill(2)} -->
<label class=\"day-card\">
  <input type=\"checkbox\">
  <span>
    <strong>Day {str(count).zfill(2)}</strong><br>
    {str(i).zfill(2)} / 11
  </span>
</label>"""
  

for i in range(1, 32):
  count += 1
  text += f"""\n<!-- Day {str(count).zfill(2)} -->
<label class=\"day-card\">
  <input type=\"checkbox\">
  <span>
    <strong>Day {str(count).zfill(2)}</strong><br>
    {str(i).zfill(2)} / 12
  </span>
</label>"""
  
for i in range(1, 16):
  count += 1
  text += f"""\n<!-- Day {str(count).zfill(2)} -->
<label class=\"day-card\">
  <input type=\"checkbox\">
  <span>
    <strong>Day {str(count).zfill(2)}</strong><br>
    {str(i).zfill(2)} / 01
  </span>
</label>"""
  
with open("./pattern.log", "w") as file:
  file.write(text)