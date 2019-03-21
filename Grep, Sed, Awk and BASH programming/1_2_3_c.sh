#!/bin/bash
ifconfig | grep -E '[a-f0-9][a-f0-9][:][a-f0-9][a-f0-9][:][a-f0-9][a-f0-9][:][a-f0-9][a-f0-9][:][a-f0-9][a-f0-9][:][a-f0-9][a-f0-9]'
