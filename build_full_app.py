# -*- coding: utf-8 -*-
import part1_head
import part2_customer
import part3_admin
import part4_modals
import part5_js

full_html = (
    part1_head.HEAD_HTML + "\n" +
    part2_customer.CUSTOMER_HTML + "\n" +
    part3_admin.ADMIN_HTML + "\n" +
    part4_modals.MODALS_HTML + "\n" +
    part5_js.JS_HTML + "\n" +
    "</body>\n</html>"
)

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

# Write to petcare360_unified.html
with open('petcare360_unified.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Successfully generated index.html and petcare360_unified.html!")
print("Total size: {} bytes, {} characters".format(len(full_html.encode('utf-8')), len(full_html)))
