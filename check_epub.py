import zipfile, os, re, sys

f = sys.argv[1]
z = zipfile.ZipFile(f)
imgs = [n for n in z.namelist() if n.startswith('OEBPS/img')]
pages = sorted([n for n in z.namelist() if n.startswith('OEBPS/p') and n.endswith('.xhtml')])
print(f'Pages: {len(pages)}')
print(f'Images: {len(imgs)}')
if imgs:
    img_size = sum(z.getinfo(n).file_size for n in imgs)
    print(f'Image total size: {img_size:,} bytes')

print()
for i in [0, 5, 10]:
    if i < len(pages):
        content = z.read(pages[i]).decode('utf-8')
        has_img = '<img' in content
        text_only = re.sub(r'<[^>]+>', '', content).strip()
        print(f'{pages[i]}: has_img={has_img}, text_length={len(text_only)}')
        if len(text_only) > 0:
            print(f'  Text: {text_only[:200]}')
        print()
