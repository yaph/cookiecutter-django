module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        less: {
            dev: {
                options: {
                    paths: ['{{cookiecutter.repo_name}}/static/styles/less']
                },
                files: {
                    '{{cookiecutter.repo_name}}/static/styles/screen.css': '{{cookiecutter.repo_name}}/static/styles/less/screen.less'
                }
            }
        },

        watch: {
            javascript: {
                files: ['{{cookiecutter.repo_name}}/static/scripts/**/*.js'],
                options: {livereload: true}
            },
            less: {
                files: '{{cookiecutter.repo_name}}/static/styles/less/**/*.less',
                tasks: ['less'],
                options: {livereload: true}
            }
        }

    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');

    grunt.registerTask('default', ['less', 'watch']);
};
