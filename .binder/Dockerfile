FROM mdzik/tclb_workspace:binder


COPY --chown=${NB_UID} . ${HOME}

RUN chown -R ${NB_UID} ${HOME}

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}
SHELL ["/bin/bash", "-c"]
ENV SHELL "/bin/bash"
USER ${NB_USER}    
ENTRYPOINT ["/bin/bash","/start"]