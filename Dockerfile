# docker build -t python-ifc .
# docker run -it python-ifc

FROM continuumio/miniconda3
RUN conda install -c conda-forge ifcopenshell
ADD ifc.py .
ADD Duplex.ifc .
CMD ["python", "ifc.py"]