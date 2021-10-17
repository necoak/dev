import sys
from pathlib import Path
import click
from pptx import Presentation
import csv

def read_pptx(pptxpath, csvwriter):
    prs = Presentation(pptxpath)
    for i, slide in enumerate(prs.slides):
        for j, shape in enumerate(slide.shapes):
            if hasattr(shape, 'text'):
                csvwriter.writerow([pptxpath, i, j, '-',  shape.text])
            elif shape.has_table:
                for k, cell in enumerate(shape.table.iter_cells()):
                    csvwriter.writerow([pptxpath, i, j, k, cell.text])

@click.command()
@click.argument('src_pptx_path')
@click.argument('out_csv_file', type=click.File(mode='w', encoding='utf_8_sig'))
def extract_text_from_pptxs(src_pptx_path, out_csv_file):
    src_pptx_files = Path(src_pptx_path).glob('**\*.pptx')
    csvwriter = csv.writer(out_csv_file, lineterminator='\n')
    csvwriter.writerow(['filename', 'slide', 'shape', 'cell', 'text'])
    for src_pptx_file in src_pptx_files:
        try:
            read_pptx(src_pptx_file, csvwriter)
        except Exception as e:
            print(str(src_pptx_file) + ' cannot read : ' + str(e), file=sys.stderr)
    return

if __name__ == '__main__':
    extract_text_from_pptxs()