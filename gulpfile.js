var gulp = require('gulp'),
    gp_concat = require('gulp-concat'),
    gp_rename = require('gulp-rename'),
    gp_uglify = require('gulp-uglify'),
    gp_sourcemaps = require('gulp-sourcemaps');

gulp.task('js-fef', function(){
  return gulp.src([
    'node_modules/jquery/dist/jquery.js', 
    'node_modules/fancybox/dist/js/jquery.fancybox.js'
    ])
    .pipe(gp_sourcemaps.init())
    .pipe(gp_concat("compiled-bundle.js"))
    .pipe(gulp.dest("content/js"))
    .pipe(gp_rename("compiled-bundle.min.js"))
    .pipe(gp_uglify())
    .pipe(gp_sourcemaps.write('./'))
    .pipe(gulp.dest('content/js'));
});

gulp.task('default', ['js-fef'], function(){});

