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

csvfile = open('.\sample.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['filename', 'slide', 'shape', 'cell', 'text'])

read_pptx(".\sample.pptx", csvwriter)